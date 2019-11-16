import feathers from "@feathersjs/feathers";
import { CounterService } from "./counterservice";
const cors = require("cors")
const mongoose = require("mongoose")
const express = require("@feathersjs/express")
const morgan = require("morgan")
const app = express(feathers())
const port: 3000 = 3000;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(morgan('combined'))
app.use(cors()); app.use(express.errorHandler());
app.configure(express.rest());
app.use("/counters", CounterService);

mongoose.connect("mongodb://localhost:27017/counter", { useUnifiedTopology: true });
const server = app.listen(port);

server.on("listening", () => {
	console.log(`server listening on PORT: ${port}`);
});
