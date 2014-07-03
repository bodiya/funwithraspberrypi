function solution( cam, num )
%SOLUTION track a specific color (default is green)
%   This function takes a camera object and number of iterations.  It takes
%   snapshots with the camera and determines the center of all the green
%   color found in the image and marks the center with a rectangluar box.
% Adapted from the Tracking a Green Ball support package example
%
%Fun with Raspberry Pi by Brian Bodiya & Tom Amlicke is licensed under a
%Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
%Based on a work at https://github.com/bodiya/funwithraspberrypi.
%
%Copyright Brian Bodiya & Tom Amlicke, 2014
for i=1:num
    img = snapshot(cam);
    
    % Separate the colors of the image into red, green, and blue
    red = img(:,:,1);
    green = img(:,:,2);
    blue = img(:,:,3);
    
    % Determine the color you want to track
    justGreen = green - red/2 - blue/2;
    
    % Determine at what level theshold is green enough
    threshold = 40;
    bw = justGreen > threshold;
    
    % Find center of object
    [x, y] = find(bw);
    if ~isempty(x) && ~isempty(y)
        xm = round(mean(x));
        ym = round(mean(y));
        xx = max(1, xm-5):min(xm+5, size(bw, 1));
        yy = max(1, ym-5):min(ym+5, size(bw, 2));
        bwbw = zeros(size(bw), 'uint8');
        bwbw(xx, yy) = 255;
        imagesc(justGreen + bwbw);
    end
   
end
    

end

