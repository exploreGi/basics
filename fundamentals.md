## AWS
- Motherboard contains CPU(Level1 cache,Level2 cache),RAM(volatile memory),HDD,etc
- RAM provides fast read and write access to data allowing the CPU to qucikly access and process the data.
- It is the computers working memory because it holds the data that is actively being used by applications.
- The closer the data is to the CPU, the faster the processing and output.(Cache>RAM>HDD)
- Data cached is processed faster than from RAM than from HDD.(Ex: vegetables from cutting board , from fridge, from grocery store) to the pot.)
## Socket
- A physical interface on a motherboard that allows the CPU to connect securely to the motherboard.
- Includes pins that make electrical connections with the CPU allowing data and power to be tranferred between CPU and other components on motherboard.
## CORE
- Independent processing unit within a CPU .
- CPU has multiple cores , allowing the CPU to execute multiple tasks simultaneously, each core executes its own set of instructions enabling parallel processing.
- AWS servers initially had SERVER_X  two 12 core (1 - 24 ) cores, then SERVER_Y two 24 core (1 - 48) cores , and SERVER_Z two 64 core(1 - 128 cores)
- Anyone, say FIRM_A requiring 30 core can rent SERVER_Y and FIRM_B can rent for remaining 18 core of  SERVER_Y, 
- The applications or users of these two FIRMS will use the same underlying physical server SERVER_Y and share the same underlying hardware resources - CPU,memory and storage.

## SMT,HT
- SMT (Simultaneous Multithreading) : keeps the processsor busy , by executing multiple threads at the same time.
- Ht (Hyper Threading) : Each physical processor core is treated as two virtual cores, each executing its own thread independently.
- Dual core processor with HT can handle four threads simultaneously(Two threads per core)

## EC2 instance stopped
Instance is temporarily turned off and not billed for instance usage , but its underlying resources are preserved, retains its state and configurations.
can be charged for any storage associated with the instance ,such as EBS volumes.

## EC2 INstance Terminated State
Instance is permanently shut down and resources are released.
