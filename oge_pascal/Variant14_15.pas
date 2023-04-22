program Variant14_15;

var
  n: integer;
  d: integer;
  count: integer;

begin
  Readln(n);
  while (n <> 0) do
  begin
    d := n mod 8;
    Writeln('Number = ', d);
    if (d = 5) then
    begin
      count += 1
    end; 
    n := n div 8;
  end;
  Writeln('count = ', count);
end.