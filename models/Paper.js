const mongoose = require("mongoose");

module.exports = mongoose.model("Paper", {
  userId: String,
  filename: String,
  tags: [String],
  uploadedBy: String,
  createdAt: { type: Date, default: Date.now }
});