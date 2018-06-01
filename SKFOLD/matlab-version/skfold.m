%% SKFOLD - Self-organizing Kohonen principal-mainFOLD-approximation map
%% Copyright (c) 2016 Emanuele Ballarin <emanuele@ballarin.cc>
%% Software released under the terms of the MIT License

%% The purpose of the script is to build and drive a Self-Organizing Map (SOM)
%% which generalizes the Principal Component Analysis (PCA) approach in the
%% elaboration of data points, arbitrarily distributed in 2 dimensions.
%% The net is bidimensional, and at the end of the self-training process it
%% displaces itself so as it lies on the principal plane that best explains
%% the overall dataset variance.
%% The net has a fixed topology and evolves following Teuvo Kohonen's
%% algorithm, in an exponentially-decaying time- and learning-rate- adaptive
%% fashion.

%% BEGINNING OF THE SCRIPT %%

% TWEAKABLE PARAMETERS
nrow = 4;            % Number of rows in the map
ncol = 50;           % Number of columns in the map

epsilon = 0.2;       % Normalized learning rate (starting)
lsigma = 18;         % Gaussian spread index (starting)

epsdecay = 0.999;    % N.L.R. (epsilon) exponential decay factor
lsigdecay = 0.96;    % G.S.I. (lsigma) exponential decay factor

thresh = 500;        % Iterations before decay enactment
effzero = 0.05;      % Learning ends when N.L.R. is equal (or less) to it

% PRELIMINARIES
neurons = rand(nrow,2,ncol);                    % Preallocation of neuron coordinates matrix (random 1x1 square)
eucl_dist = zeros(nrow,ncol);                   % Preallocation of neuron Euclidean distances matrix (zeros)
manh_dist = zeros(nrow,ncol);                   % Preallocation of neuron Manhattan distances matrix (zeros)
f_matrix = zeros(nrow,ncol);                    % Preallocation of neuron F-matrix (zeros)
wgt_add = zeros(nrow,2,ncol);                   % Preallocation of neuron additive matrix (zeros)
neurons_sparseplot = zeros(nrow*ncol,2);        % Preallocation of neuron matrix to save to file (sparse plot)


% DATA ACQUISITION
original_dataset = importdata('datagen.txt');       % Copies the dataset matrix in a MATLAB matrix
npoints = size(original_dataset,1);                 % Computes the number of points in the dataset (rows)

% NEURAL DRIVE
% Indexes initialization
iteration = 0;
threshold = thresh;
runagain = true;

% parpool         % The parallel cluster and pool is loaded and initialized

while runagain
    %
    while iteration < threshold

        examplenr = randi([1 npoints],1,1);         % Extract a random example from dataset
        example = original_dataset(examplenr,:);    % Example coordinates

        % Distance matrix building
        parfor n = 1:ncol
            for m = 1:nrow
                eucl_dist(m,n) = sqrt(sum((example-neurons(m,:,n)).^2));
            end
        end

        % Winner neuron challenge (NOT PARALLELIZABLE)
        best_distance = flintmax;    % Biggest possible float available
        for n = 1:ncol
            for m = 1:nrow
                if eucl_dist(m,n) < best_distance
                    best_distance = eucl_dist(m,n);
                    manh_winner = [m n];
                end
            end
        end

        % Manhattan matrix building
        parfor n = 1:ncol
            for m = 1:nrow
                manh_dist(m,n) = sum((manh_winner - [m n]).^2);
            end
        end

        % F-coefficient matrix building (VECTORIZED)
        f_matrix = exp(manh_dist/(-2*(lsigma^2)));

        % Weight update additive matrix building
        parfor n = 1:ncol
            for m = 1:nrow
                wgt_add(m,:,n) = epsilon*(example - neurons(m,:,n))*f_matrix(m,n);
            end
        end

        % Weight update, summation (VECTORIZED)
        neurons = neurons + wgt_add;


        iteration = iteration + 1;   % Iteration counter update

    end

% Outer cycle follows here...

    disp(['Completed iteration N° ' num2str(iteration)])

    % Stop condition is evaluated
    if epsilon <= effzero
        runagain = false;
    end

    % Update parameters
    epsilon = epsilon*epsdecay;
    lsigma = lsigma*lsigdecay;

    threshold = threshold + thresh;

end

% DATA OUTPUT (NOT PARALLELIZABLE)
for n = 1:ncol
    for m = 1:nrow
        neurons_sparseplot((nrow*(n-1) + m),:) = neurons(m,:,n);
    end
end

% Writing to file
disp('Writing to file...')
save('reduced-dataset.txt', 'neurons_sparseplot', '-ASCII');
disp(' ')
disp('Done. Execution successful!')

%% END OF THE SCRIPT %%
