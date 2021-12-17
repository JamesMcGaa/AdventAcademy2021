import os 
f = open("input16.txt", "r")
input_cast = f.readline().strip()
# res = "{0:08b}".format(int(input_cast, 16))
res = ''.join(bin(int(c, 16))[2:].zfill(4) for c in input_cast)
print(res)

def process_packet(ind, res, end_ind = len(res)):
    global global_counter
    global_counter = 0
    while ind < len(res) and ind < end_ind:
        try:
            print(ind)
            packet_version = int(res[ind:ind+3], 2)
            global_counter += packet_version
            type_id = int(res[ind+3:ind+6], 2)
            ind += 6
            print(packet_version, type_id)
            if type_id == 4: #literal
                binary_literal_str = ""
                while True:
                    terminal = res[ind] == "0"
                    binary_literal_str += res[ind+1:ind+5]
                    ind += 5
                    if terminal:
                        break
                # ind += 3 - ind % 4
                print("literal", int(binary_literal_str, 2))
                # return int(binary_literal_str, 2)

            
            else: #operator
                length_type_id = res[ind]
                ind += 1
                if length_type_id == "0": # subpackets total bits = next 15 bits
                    total_subpacket_len = str(int(res[ind:ind+15],2))
                    ind += 15
                    
                
                else: # total subpackets = next 11 bits
                    total_subpackets = str(int(res[ind:ind+11],2))
                    ind += 11
        except:
            print('sadge')
            break
process_packet(0, res)
print(global_counter)