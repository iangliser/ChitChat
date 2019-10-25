%Warning: this code is barely working and will crash more often than not
%All credit is due to Ethan Murray who posted the prototype code found here:
%mathworks.com/matlabcentral/answers/329166-plotting-random-points-within-boundary


for i = 1: 40
    figure('units','normalized','outerposition',[0 0 1 1])
    n = randi(20,70)
    R = 2;
    x0 = 0; % Center of the circle in the x direction.
    y0 = 0; % Center of the circle in the y direction.
    % Now create the set of points.
    t = 2*pi*rand(n,1);
    r = R*sqrt(rand(n,1));
    x = x0 + r.*cos(t);
    y = y0 + r.*sin(t);
    % Now display our random set of points in a figure.
    plot(x,y, 's', 'MarkerSize', 10, 'MarkerEdgeColor',[0,0,0]); hold off
    axis off
    fig = gcf;
    namer = sprintf('%i', i)
    fig.PaperPositionMode = 'auto';
    print(namer,'-dpng','-r0')
end