The "Busiest Time in The Mall" Problem

The mall management is trying to evaluate the busiest moment in the mall on the last year.
You are given data from the door detectors: each data entry includes time stamp in seconds (in Unix Epoch format), amount of people and whether they entered or exited.

Example of a data entry:
{ time: 1440084737,  count: 4,  type: "enter" }

Find what was the busiest period in the mall on the last year. Return an array with two Epoch timestamps representing the beginning and end of that period. You may assume that the data your are given is accurate and that each second with entries or exists is recorded. Implement the most efficient solution possible and analyze its time and space complexity.


def pramp():
   print "Practice Makes Perfect"

pramp()


Example:
{ time: 1440084737,  count: 4,  type: "enter" } -- Day1
{ time: 1440084738,  count: 4,  type: "enter" }
{ time: 1440084739,  count: 4,  type: "exit" }  -- Day1
{ time: 1440084747,  count: 4,  type: "enter" }- Day 2
{ time: 1440084757,  count: 4,  type: "exit" }- Day 2

{ time: 1440084767,  count: 4,  type: "exit" }- Day 3 
{ time: 1440084767,  count: 4,  type: "exit" }- Day 3

HashMap[<Day, Month>, number of people on this day ]
enter_counter = 0
enter_counter += enter_counter
exit_counter += exit_counter

//End of day 
enter_counter
enter_counter > exit_counter

day_list:    one entry: <enter_counter, timestamp1, timestamp2>
      
iterate on day_list find the max enter_counter. 


diff_for_next_day + enter_counter


def find_max(list_of_data_entry):
   
   prevDay = None
   currentDay = None
   enter_counter = 0
   exit_counter = 0
   diff_counter = 0
   day_list = []
   ts1 = None
   ts2 = None
   
   for d in list_of_data_entry:
      time = d["time"]
      count = d["count"]
      type = d["type"]
      
      currentDay = get_current_day(time)
      if prevDay == None or prevDay == currentDay:
         if type == "enter":
            enter_counter += count
            if ts1 == None:
               ts1 = time
         if type == "exit":
            exit_counter += count
            ts2 = time
      elif prevDay != currentDay:
         # new day
         #this is new day, reinitalize the variables and also store enter counter
         day_list.append((enter_counter+diff_counter, ts1, ts2))
         
         diff_counter = enter_counter - exit_counter
         enter_counter = 0
         exit_counter = 0
         ts1 = None
         ts2 = None
         if type == "enter":
            enter_counter += count
            if ts1 == None:
               ts1 = time
         if type == "exit":
            exit_counter += count
            
            ts2 = time
               
      prevDay = currentDay
         
   max_ts = None
   max_counter = -1000
   
   for i in day_list:
      max_counter = max(i[0], max_counter)
      if max_counter == i[0]:
         max_ts = ((i[1], i[2]))
         
   return max_ts

trllgrn@gmail.com