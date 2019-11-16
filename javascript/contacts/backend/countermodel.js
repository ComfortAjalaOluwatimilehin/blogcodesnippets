"use strict";
exports.__esModule = true;
var mongoose = require("mongoose");
var CounterSchema = mongoose.schema({
    value: mongoose.Types.number
});
exports.CounterModel = mongoose.Model("Counter", CounterSchema);
