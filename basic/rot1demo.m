clear; close all; clc;
vehi= [0, 1, 1, -1, -1, 0 ;2, 1, -1, -1,1,2];
for theta=0:0.05:2*pi/3
  R=[cos(theta),-sin(theta);sin(theta),cos(theta)];
  newvehi=R*vehi;
  plot(newvehi(1,:),newvehi(2,:));
  axis equal;axis ([-10,10,-10,10]);
  drawnow;
end