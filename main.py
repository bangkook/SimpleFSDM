import ParseInput
import commands


args = ParseInput.parse_args()
    
if(args.command == "CREATE"): 
   commands.create(args.schema)

if(args.command == "SET"):
   print(commands.set(args.database, args.table, args.primary_key, args.value))

if(args.command == "GET"):
   print(commands.get(args.database, args.table, args.primary_key, args.value))

if(args.command == "DELETE"):
   commands.delete(args.database, args.table, args.primary_key, args.value)

