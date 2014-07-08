function ShowI2CBuses( rpi )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
for i = 1:length(rpi.AvailableI2CBuses)
    disp(rpi.AvailableI2CBuses{i})
    scanI2CBus(rpi, rpi.AvailableI2CBuses{i})
end


end

