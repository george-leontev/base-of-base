program Variant11_15;

var
  k: integer;
  n: integer;
  min := 30001;

begin
  Readln(k);
  for var x := 0 to k - 1 do
  begin
    Readln(n);  
    if (n > 150) and (n < min) then
    begin
      min := n
    end;
  end;
  Writeln('min = ', min);
end.