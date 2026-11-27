(() => {
    const baseUrl = (document.body.dataset.baseUrl || "").replace(/\/$/, "");
    const modal = document.getElementById("search-modal");
    const trigger = document.getElementById("search-trigger");
    const input = document.getElementById("search-input");
    const statusEl = document.getElementById("search-status");
    const resultsEl = document.getElementById("search-results");
    const nav = document.querySelector(".site-nav");
    const activeLink = nav?.querySelector("[aria-current=page]");

    if (activeLink && activeLink.getBoundingClientRect().right > nav.getBoundingClientRect().right) {
        nav.scrollLeft += activeLink.getBoundingClientRect().left - nav.getBoundingClientRect().left;
    }

    let indexData = null;
    let indexPromise = null;
    let lastFocused = null;

    function loadIndex() {
        if (indexData) return Promise.resolve(indexData);
        if (indexPromise) return indexPromise;
        statusEl.textContent = "Loading intelligence index...";
        indexPromise = fetch(`${baseUrl}/data/content.json`)
            .then((resp) => {
                if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
                return resp.json();
            })
            .then((data) => {
                indexData = Array.isArray(data) ? data.map((item) => ({
                    ...item,
                    searchText: `${item.t} ${item.c} ${(item.g || []).join(" ")} ${item.s || ""}`.toLowerCase(),
                })) : [];
                return indexData;
            })
            .catch(() => {
                indexPromise = null;
                statusEl.textContent = "Failed to load search index.";
                return [];
            });
        return indexPromise;
    }

    function renderResults(query) {
        if (!indexData) return;
        const q = query.trim().toLowerCase();
        resultsEl.textContent = "";

        if (!q) {
            statusEl.textContent = `${indexData.length} indexed records ready. Type to filter.`;
            return;
        }

        const terms = q.split(/\s+/).filter(Boolean);
        const matches = [];
        for (let i = 0; i < indexData.length; i++) {
            const item = indexData[i];
            const hay = item.searchText;
            let ok = true;
            for (let j = 0; j < terms.length; j++) {
                if (!hay.includes(terms[j])) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                matches.push(item);
                if (matches.length >= 40) break;
            }
        }

        statusEl.textContent =
            matches.length >= 40
                ? "Showing top 40 matches"
                : `${matches.length} match${matches.length === 1 ? "" : "es"}`;

        const frag = document.createDocumentFragment();
        for (const item of matches) {
            const li = document.createElement("li");
            const a = document.createElement("a");
            a.href = item.u;

            const titleSpan = document.createElement("span");
            titleSpan.textContent = item.t;

            const metaSpan = document.createElement("span");
            metaSpan.className = "search-result-meta";
            const parts = [item.c];
            if (item.k) parts.push("KEV");
            if (item.s) parts.push(item.s);
            if (item.d) parts.push(item.d);
            metaSpan.textContent = parts.join(" · ");

            a.appendChild(titleSpan);
            a.appendChild(metaSpan);
            li.appendChild(a);
            frag.appendChild(li);
        }
        resultsEl.appendChild(frag);
    }

    function openSearch(initialQuery = "") {
        if (!modal) return;
        if (modal.hidden) lastFocused = document.activeElement;
        modal.hidden = false;
        modal.setAttribute("aria-hidden", "false");
        if (initialQuery) {
            input.value = initialQuery;
        }
        input.focus();
        loadIndex().then(() => renderResults(input.value));
    }

    function closeSearch() {
        if (!modal || modal.hidden) return;
        modal.hidden = true;
        modal.setAttribute("aria-hidden", "true");
        if (lastFocused && typeof lastFocused.focus === "function") {
            lastFocused.focus();
        }
    }

    if (trigger) {
        trigger.addEventListener("click", () => openSearch());
    }

    document.querySelectorAll("[data-close-search]").forEach((el) => {
        el.addEventListener("click", closeSearch);
    });

    document.querySelectorAll("[data-search-tag]").forEach((btn) => {
        btn.addEventListener("click", () => openSearch(btn.dataset.searchTag || ""));
    });

    if (input) {
        input.addEventListener("input", () => renderResults(input.value));
    }

    document.addEventListener("keydown", (e) => {
        if (e.key === "Tab" && modal && !modal.hidden) {
            const focusable = modal.querySelectorAll("input, button, a[href]");
            const boundary = e.shiftKey ? focusable[0] : focusable[focusable.length - 1];
            if (document.activeElement === boundary || !modal.contains(document.activeElement)) {
                e.preventDefault();
                (e.shiftKey ? focusable[focusable.length - 1] : focusable[0]).focus();
            }
        } else if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
            e.preventDefault();
            if (modal && !modal.hidden) closeSearch();
            else openSearch();
        } else if (e.key === "/" && !e.ctrlKey && !e.metaKey && !e.altKey) {
            const tag = (document.activeElement?.tagName || "").toLowerCase();
            if (tag !== "input" && tag !== "textarea") {
                e.preventDefault();
                openSearch();
            }
        } else if (e.key === "Escape") {
            closeSearch();
        }
    });

    // Lightweight intent-based prefetch (respects Save-Data)
    const saveData = navigator.connection && navigator.connection.saveData;
    if (!saveData) {
        const prefetched = new Set();
        let hoverTimer = null;
        document.addEventListener("pointerover", (e) => {
            const anchor = e.target.closest && e.target.closest("a[href]");
            if (!anchor) return;
            const href = anchor.getAttribute("href");
            if (!href || !href.startsWith(baseUrl + "/") || prefetched.has(href)) return;
            clearTimeout(hoverTimer);
            hoverTimer = setTimeout(() => {
                prefetched.add(href);
                const link = document.createElement("link");
                link.rel = "prefetch";
                link.href = href;
                document.head.appendChild(link);
            }, 75);
        });
    }
})();
