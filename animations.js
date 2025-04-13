document.getElementById("simplify-btn").addEventListener("click", async () => {
    const topic = document.getElementById("topic").value.trim(); // Get the topic input
    const outputDiv = document.getElementById("output");
    const conceptText = document.getElementById("concept-text");

    if (!topic) {
        alert("Please enter a topic!");
        return;
    }

    try {
        const response = await fetch("/simplify", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ topic }), // Send the topic to the backend
        });

        if (response.ok) {
            const data = await response.json();
            conceptText.textContent = data.concept || "No concept found."; // Display the response
            outputDiv.classList.remove("hidden");
            outputDiv.classList.add("animate-fade-in");
        } else {
            alert("Failed to fetch the concept. Please try again.");
        }
    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred. Please try again.");
    }
});