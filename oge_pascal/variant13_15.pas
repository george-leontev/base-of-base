program Variant13_15;
var
  k: integer;
  n: integer;
  min := 30001;
begin
  Readln(k);
  for var x := 0 to k - 1 do
  begin
    Readln(n);
    if (n mod 16 = 0) then
    begin
      if (n < min) then
      begin
        min := n
      end;
    end;
  end;
  writeln('min = ',min)
end.