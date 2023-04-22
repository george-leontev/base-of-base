program Variant6_15;

var
  k: integer;
  n: integer;
  count: integer;

begin
  Readln(k);
  for var x := 0 to k - 1 do
  begin
    Readln(n);
    if (n mod 221 < 7) then
    begin
      count := count + 1
    end;
  end;
  Writeln('count = ', count);
end.
