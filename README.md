# Hurricane Loss Model

Hurricane loss model to estimate expected annual economic loss.

## Requirement
Execute the following command in linux container
```
usage: gethurricaneloss [options] florida_landfall_rate florida_mean florida_stddev
gulf_landfall_rate gulf_mean gulf_stddev
```

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
    gethurricaneloss 3 0.55 0.42 6 0.45 0.33 --n=100
   ```
5. For help on understanding the parameters, type the following command.
       
    ```
    gethurricaneloss -h
    ```
        
    ```
    positional arguments:
    florida_landfall_rate Annual rate of land-falling hurricanes in Florida
    florida_mean          Florida LogNormal parameter mean
    florida_stdev         Florida LogNormal parameter std deviation
    gulf_landfall_rate    Annual rate of land-falling hurricanes in Gulf states
    gulf_mean             Gulf states LogNormal parameter mean
    gulf_stdev            Gulf states LogNormal parameter stdev
    
    optional arguments:
      --n N               Number of Monte Carlo Simulations
      ```
       
      ![gethurricaneloss](img/help.png?raw=true)
6. Print the hurricaneloss.log. It's stored in the root directory (same level as gethurricaneloss.py file).
    ```
    cat hurricaneloss.log
    ```      
   
