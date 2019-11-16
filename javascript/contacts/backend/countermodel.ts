const mongoose = require("mongoose")



const CounterSchema = mongoose.schema({
    value: mongoose.Types.number
})



export const CounterModel = mongoose.Model("Counter", CounterSchema)