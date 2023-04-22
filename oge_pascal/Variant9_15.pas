program Variant9_15;

var
  k: integer;
  n: integer;

begin
  Readln(k);
  for var x := 0 to k - 1 do
  begin
    Readln(n);
    if (n mod 2 = 0) then
    begin
      Writeln(x);
    end;
  end;
end.