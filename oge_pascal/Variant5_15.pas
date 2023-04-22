program Variant5_15;

var
  k: integer;
  n: integer;
  a: integer;
  count: integer;

begin
  Readln(k);
  for var x := 0 to k - 1 do
  begin
    Readln(n);
    if (a < 700) then
    begin
      a := a + n;
      count := count + 1
    end;
  end;
  Writeln('count = ', count);
end.