const express = require("express");
const cors = require("cors");
const fs = require("fs");
const path = require("path");

const app = express();
const PORT = 4000;

app.use(cors()); // ✅ Now app is defined, so no error
app.use(express.json()); // ✅ Middleware to parse JSON data

app.post("/save", (req, res) => {
    const data = req.body.message + "\n"; // Append newline for multiple entries
    console.log("📩 Received Data:", data); // Log received data

    const filePath = path.join(__dirname, "data.txt"); // Ensure correct file path

    fs.appendFile(filePath, data, (err) => {
        if (err) {
            console.error("❌ Error writing to file:", err);
            return res.status(500).send("Error saving data.");
        }
        console.log("✅ Data saved successfully to data.txt");
        res.send("Data saved successfully!");
    });
});

app.listen(PORT, () => console.log(`🚀 Server running on http://localhost:${PORT}`));
