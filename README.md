# Hurricane Loss Model

Hurricane loss model to estimate expected annual economic loss.

## Instructions
1. Clone the repository and cd into the root directory.
2. Build the python / linux container.
    ``` 
    docker build -t oasis-assignment .
    ```
3. Run the container's bash shell
    ```
    docker run -it oasis-assignment /bin/bash
    ```
4. Call the hurricane model.
   
   ```
    hurricaneloss 0.4 0.5 0.6 0.7 100
   ```
5. For help on understanding the parameters, type the following command
   ```
    hurricaneloss -h
   ```
   
    ![gethurricaneloss](img/help.png?raw=true)
   
   
