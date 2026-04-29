const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
require("dotenv").config();

const authMiddleware = require("./middleware/authMiddleware");

const app = express();

// middlewares
app.use(express.json());
app.use(cors());

// basic route
app.get("/", (req, res) => {
  res.send("Semantix AI Backend Running 🚀");
});

// 🔐 PROTECTED ROUTE
app.get("/api/protected", authMiddleware, (req, res) => {
  res.send("You are authorized 🎉");
});

// existing routes
app.use("/api/auth", require("./routes/auth"));
app.use("/api/papers", require("./routes/papers"));

// DB connection
mongoose
  .connect(process.env.MONGO_URI)
  .then(() => console.log("DB Connected ✅"))
  .catch((err) => console.log(err));

// start server
app.listen(5000, () => {
  console.log("Server running on 5000 🚀");
});