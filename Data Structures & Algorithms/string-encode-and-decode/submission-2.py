class Solution:

    def encode(self, strs: List[str]) -> str:
        track_arr = []
        encoded_arr = []
        for s in strs:
            encoded_arr.append( str(len(s)) )
            encoded_arr.append("#")
            encoded_arr.append(s)

        return "".join(encoded_arr)
        # return "#".join(strs)

    def decode(self, s: str) -> List[str]:
        encoded_arr = list(s)
        print(encoded_arr)
        decoded_arr = []

        last_processed_index = -1
        i = 0
        while i < len(encoded_arr):
           
            if encoded_arr[i] == "#":
                num_arr = []
                for j in range(i-1, last_processed_index, -1): # stop at -1 so that it will catch the digit in index 0
                    # check for the number before the delimiter
                    if (encoded_arr[j].isdigit() == True):
                        num_arr.insert(0, encoded_arr[j])
                    else:
                        break

                print(num_arr)
                len_of_str = int("".join(num_arr))

                str_arr = []
                for h in range(i+1, i+1+len_of_str):
                    str_arr.append(encoded_arr[h])
                
                word = "".join(str_arr)

                decoded_arr.append(word)

                # increament and state management
                i += (len_of_str+1) # so it skip the copied word to the next incase a delimiter is part of the original word

                # Set the wall at the end of the word we just jumped over
                last_processed_index = i - 1
                
            else:
                i += 1

        return decoded_arr