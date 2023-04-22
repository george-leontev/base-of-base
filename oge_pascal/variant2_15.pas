program Variant2_15;

var
  k: integer;
  n: integer;
  sum := 0;

begin
  Readln(k);
  for var x := 0 to k - 1 do
  begin
    Readln(n);
    if (n mod 10 <> 3) and (n <= 25) then
      sum := sum + n
  end;
  Writeln('sum = ', sum)
end.