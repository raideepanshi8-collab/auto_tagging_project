const express = require("express");
const router = express.Router();
const auth = require("../middleware/authMiddleware");

// UPLOAD
router.post("/upload", auth, (req, res) => {
  res.json({ message: "PDF uploaded successfully" });
});

// BULK UPLOAD
router.post("/bulk", auth, (req, res) => {
  res.json({ message: "ZIP uploaded successfully" });
});

module.exports = router;