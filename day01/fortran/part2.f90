program part1
   implicit none
   ! character(len=*), parameter :: fname = "example.txt"
   character(len=*), parameter :: fname = "input.txt"
   character(len=10) :: line
   character :: direction
   integer :: steps
   integer :: unit, ios, i
   integer :: value = 50
   integer :: zeros = 0

   ! Open the file
   open(newunit=unit, file=fname, status="old", action="read", iostat=ios)
   if (ios /= 0) then
      print *, "Error: cannot open file"
      stop 1
   end if

   ! Loop over lines
   do
      read(unit, '(a)', iostat=ios) line
      if (ios /= 0) then
         exit
      end if
      direction = line(1:1)
      read(line(2:), *) steps
      do i = 1, steps
         if (direction == 'L') then
            value = value - 1
            if (value < 0) then
               value = 99
            end if
         else if (direction == 'R') then
            value = value + 1
            if (value > 99) then
               value = 0
            end if
         end if
         if (value == 0) then
            zeros = zeros + 1
         end if
      end do
   end do
   print '(i0)', zeros
end program part1
