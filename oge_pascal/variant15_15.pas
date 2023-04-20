program Variant15_15;
var
  k: integer;
  n: integer;
  sum := 0;
  begin
    Readln(k);
    begin
      for var x := 0 to k - 1 do
      begin
        Readln(n);
        if (n < 50) and (n > 10) then
        begin
          sum := sum + n
        end;
      end;
    end;
    Writeln('Sum = ', sum)
  end.