
# Node Based Structure
### Publish / Subscribe Model

All of the nodes are modular, and publish / recieve data from a topic (kind of like Kafka at RFA).

This means that there are also public, open source nodes that can have out-of-the-box functionality, since they are independent fromt he rest of the program.

Also, multiple nodes can publish to the same topic.

### Example: Displaying temperature data
Instead of running a loop and recording data, and then displaying it, this will run them both seperately, isolating both processes into their own nodes. This way, if the display breaks, then the data will still be recorded. Also, another system (that maybe only wants every 5 temperature readings) could subscribe to this topic without changing the structure or timing of the original.

### Services
When the publisher model doesn't work (when direct communication is required, often for something that only occurs occaisonaly, or the timing is important), then a service can be used. This will coordinate the timing of the transaction.

### Actions
Actions are similar to services, but serves as communication for long-running tasks. This will allow another node to continue running, while monitoring the progress / completion status of another node.

### Parameters
They allow you to modify params to a node during running, for testing. This will change things like speed, sampling rate, etc.