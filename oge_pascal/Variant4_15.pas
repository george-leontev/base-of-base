program variant4_15;


var
  k: integer;
  number: integer;
  n: integer;
  sum := 0;
  d: integer;
  count: integer;

begin
  Readln(k);
  
  
  for var x := 0 to k - 1 do
  begin
    
    Readln(number);
    count := 0;
    n := number;
    
    while (n <> 0) do
    begin
      d := n mod 10;
    
      if (d = 5) then
      begin
        count += 1;
        break;
      end;
      
      n := n div 10;
    end;
    
    if (number <= 16) and (count = 0) then
    begin
      sum := sum + number;
    end;
    
  end;
  
  Writeln('sum = ', sum);
end.