function analyze() {
    const text = document.getElementById("inputText").value;

    fetch("/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    })
        .then(res => res.json())
        .then(data => {
            document.getElementById("result").style.display = "block";

            document.getElementById("verdict").innerText = data.verdict;
            document.getElementById("message").innerText = data.message;
            document.getElementById("confidence").innerText = data.confidence;

            const list = document.getElementById("sources");
            list.innerHTML = "";

            if (data.sources.length === 0) {
                list.innerHTML = "<li>No matching global news articles found.</li>";
            }

            data.sources.forEach(s => {
                const li = document.createElement("li");
                li.innerHTML = `
                <a href="${s.url}" target="_blank">
                    ${s.title} — ${s.source}
                </a>
            `;
                list.appendChild(li);
            });
        });
}
