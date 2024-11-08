async function submitCode() {
    const code = document.getElementById("code").value;

    const response = await fetch('/parse', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code }),
    });

    const result = await response.json();
    document.getElementById("astOutput").innerText = JSON.stringify(result.ast, null, 2);
}
