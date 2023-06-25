import subprocess
import time
import os
import signal
import pickle

bitcoin_address = 'bc1qus09g0n5jwg79gje76zxqmzt3gpw80dcqspsmm'


# Function to save the checkpoint
def save_checkpoint(start_keyspace, end_keyspace):
    checkpoint_data = {
        'start_keyspace': start_keyspace,
        'end_keyspace': end_keyspace
    }
    with open('checkpoint.pkl', 'wb') as f:
        pickle.dump(checkpoint_data, f)

# Function to load the checkpoint
def load_checkpoint():
    if os.path.exists('checkpoint.pkl'):
        with open('checkpoint.pkl', 'rb') as f:
            checkpoint_data = pickle.load(f)
        return checkpoint_data['start_keyspace'], checkpoint_data['end_keyspace']
    else:
        return '70000000000000000', '70100000000000000'

def run_vbcr(start_keyspace, end_keyspace):
    output_filename = f'{start_keyspace[:3]}.txt'  # Generate the output filename based on the start keyspace
    command = f'VBCr.exe -t 3 -gpu -gpuId 0 -begr {start_keyspace} -endr {end_keyspace} -o {output_filename} -drk 1 -dis 1 -c 1BY8GQbnu'

    process = subprocess.Popen(command, shell=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
    time.sleep(500)  # Wait for 500 seconds
    os.kill(process.pid, signal.CTRL_BREAK_EVENT)  # Send CTRL_BREAK_EVENT signal to terminate the process group
    process.wait()  # Wait for the process to exit

# Load the checkpoint if it exists, otherwise start from the beginning
start_keyspace, end_keyspace = load_checkpoint()

# Loop until explicitly interrupted
last_save_time = time.time()  # Track the last save time
save_interval = 60  # Save interval in seconds (1 minute)

while True:
    try:
        increment = '100000000000000'  # Increment value

        while int(end_keyspace, 16) <= int('800ffffffffffffff', 16):  # Continue until the ending keyspace value is reached
            run_vbcr(start_keyspace, end_keyspace)
            start_keyspace = hex(int(end_keyspace, 16) + 1)[2:]  # Increment the start keyspace value
            end_keyspace = hex(int(start_keyspace, 16) + int(increment, 16) - 1)[2:]  # Increment the end keyspace value correctly

            # Save the checkpoint every minute
            current_time = time.time()
            elapsed_time = current_time - last_save_time
            if elapsed_time >= save_interval:
                save_checkpoint(start_keyspace, end_keyspace)
                last_save_time = current_time

            time.sleep(5)  # Wait for 5 seconds before restarting
    except KeyboardInterrupt:
        save_checkpoint(start_keyspace, end_keyspace)  # Save the checkpoint if interrupted by KeyboardInterrupt
        break

# Restart the program with the original starting values
start_keyspace, end_keyspace = load_checkpoint()

# Continue program execution from the last saved checkpoint
while int(end_keyspace, 16) <= int('3ffffffffffffffff', 16):
    run_vbcr(start_keyspace, end_keyspace)
    start_keyspace = hex(int(end_keyspace, 16) + 1)[2:]
    end_keyspace = hex(int(start_keyspace, 16) + int(increment, 16) - 1)[2:]
