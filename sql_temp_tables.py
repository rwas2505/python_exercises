list = [
  ["Foster City", 50 ],
  ["Fresno Armstrong Ave", 5 ],
  ["Livermore", 20 ],
  ["Martinez", 60 ],
  ["Milpitas", 45 ],
  ["Parker", 20 ],
  ["Petaluma", 75 ],
  ["Portland", 15 ],
  ["Reno Capital Blvd", 5 ],
  ["Sacramento", 40 ],
  ["Salt Lake City WH", 5 ],
  ["Seattle-Temp", 5 ],
  ["Stockton", 10 ],
  ["Albuquerque", 5 ],
  ["Atwater Village", 10 ],
  ["Austin WH", 10 ],
  ["Dallas", 10 ],
  ["Hawthorne", 15 ],
  ["Inland Empire", 15 ],
  ["Irvine", 25 ],
  ["Phoenix Pinnacle Peak", 15 ],
  ["San Diego", 25 ],
  ["San Fernando Valley", 40 ],
  ["Santa Maria", 15 ],
  ["Sugarland", 10 ],
  ["Vista", 15 ],
  ["West Las Vegas", 10 ],
  ["Beltsville", 35 ],
  ["Bethpage", 10 ],
  ["Burlington", 5 ],
  ["Chicago X", 5 ],
  ["Fort Lauderdale", 10 ],
  ["Hartford", 10 ],
  ["Marlborough", 10 ],
  ["New Windsor", 5 ],
  ["Norristown", 5 ],
  ["Orlando", 20 ],
  ["Pine Brook", 5 ],
  ["Pittsburgh", 5 ],
  ["Raynham", 15 ],
  ["Seaford", 5 ],
  ["Tampa", 20 ],
  ["Wilmington Ballardva",10],
]

# Python3 code to remove whitespace 
def remove(string): 
    return "".join(string.split()) 

for entry in list:
  warehouse = entry[0]
  temp_table = remove(warehouse)
  (f"--{entry}")
  print(f"IF OBJECT_ID('tempdb..#{temp_table}') IS NOT NULL BEGIN DROP TABLE #{temp_table} END")
  print(f"SELECT TOP {entry[1]}*")
  print(f"INTO #{temp_table}")
  print("FROM #ALLJOBS")
  print(f"WHERE office in('{warehouse}')")
  print("")
  print("")


  # USEFUL RESOURCES
  # iterate through array: https://snakify.org/en/lessons/two_dimensional_lists_arrays/
  # string interpolation: https://realpython.com/python-string-formatting/
  # white space handling: journaldev.com/23763/python-remove-spaces-from-string
  # https://www.geeksforgeeks.org/python-remove-spaces-from-a-string/