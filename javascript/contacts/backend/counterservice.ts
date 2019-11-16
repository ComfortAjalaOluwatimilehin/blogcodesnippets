
import { CounterModel } from "./countermodel"

class CounterServiceInstance<Application> {

    async  find() {
        // GET /counters
        try {
            let counter = await CounterModel.findOne()
            return { document: counter }
        } catch (err) {
            return { ...err }
        }
    }
    update() { }

}


export const CounterService = new CounterServiceInstance()