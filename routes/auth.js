const express = require("express");
const router = express.Router();

// TEMP STORAGE (no DB for now)
let users = [];

// REGISTER
router.post("/register", (req, res) => {
  const { email, password } = req.body;

  if (!email || !password) {
    return res.status(400).json({ message: "Fill all fields" });
  }

  users.push({ email, password });

  res.json({ message: "Registered successfully" });
});

// LOGIN
router.post("/login", (req, res) => {
  const { email, password } = req.body;

  const user = users.find(u => u.email === email && u.password === password);

  if (!user) {
    return res.status(401).json({ message: "Invalid credentials" });
  }

  res.json({
    token: "user-token-" + email
  });
});

module.exports = router;