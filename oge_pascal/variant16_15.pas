program Variant16_15;

var
  k: integer;
  n: integer;
  sum := 0;

begin
  Readln(k);
  for var x := 0 to k - 1 do
  begin
    Readln(n);
    if (n < 10) or (n > 50) then
    begin
      sum := sum + n
    end;
  end;
  Writeln(sum);  
end.