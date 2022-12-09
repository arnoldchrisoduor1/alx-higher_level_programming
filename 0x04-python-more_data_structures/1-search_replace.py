#!/usr/bin/python3
def search_replace(my_list, search, replace):

      # Create a new list with the same size as the input list

        new_list = [0 for i in range(len(my_list))]



          # Loop through each element in the input list

            for i in range(len(my_list)):

                    # If the element is equal to the search element, add the replace element to the new list

                        if my_list[i] == search:

                                  new_list[i] = replace

                                      # Otherwise, add the element from the input list to the new list

                                          else:

                                                    new_list[i] = my_list[i]



                                                      # Return the new list

                                                        return new_list


