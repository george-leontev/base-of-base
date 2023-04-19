program Variant17_15;

var
  n1: integer;
  n := 1;
  count := 0;

begin
  Readln(n1);
  while (n * 2 < n1) do
  begin
    count := count + 1;
    n := n * 2
  end;
  Writeln(count);
end.