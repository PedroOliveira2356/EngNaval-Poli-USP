%==========================================================================
% UNIFIED WAVE GENERATION AND ANALYSIS SCRIPT
% 
% Description: This script generates and plots decaying cosine waves with
%              optional random noise components, demonstrating different
%              sampling and parameter configurations.
%
% Features:
%   - Two distinct wave generation configurations
%   - Proper commenting and documentation
%   - Efficient vectorized operations
%   - Professional visualization
%   - Configurable parameters
%
% Author: [Your Name]
% Date: [Current Date]
% Version: 1.0
%==========================================================================

clear
close all
clc

%% CONFIGURATION PARAMETERS
% Define all configurable parameters in one section for easy modification

% Common parameters
COMMON.frequency = 1;           % Frequency of the wave (Hz)
COMMON.duration = 100;          % Duration of the wave (seconds)

% Configuration 1 parameters (undersampled with noise)
CONFIG1.samplingRate = 1.2;     % Sampling rate (Hz) - intentionally low
CONFIG1.decayRate = 0.01;       % Amplitude decay rate
CONFIG1.noiseLevel = 0.125;     % Random noise amplitude (1/8)
CONFIG1.amplitudeScale = 1.5;   % Amplitude scaling factor

% Configuration 2 parameters (properly sampled, no noise)
CONFIG2.samplingRate = 1;       % Sampling rate (Hz)
CONFIG2.decayRate = 0.1;        % Amplitude decay rate
CONFIG2.noiseLevel = 0;         % No random noise
CONFIG2.amplitudeScale = 1;     % No amplitude scaling

%% GENERATE CONFIGURATION 1: UNDERSAMPLED WAVE WITH NOISE
fprintf('Generating Configuration 1: Undersampled wave with noise...\n');

% Time vector for configuration 1
t1 = 0:1/CONFIG1.samplingRate:COMMON.duration;

% Calculate amplitude with exponential decay
amplitude1 = exp(-CONFIG1.decayRate * t1);

% Generate random noise vector
rng(42); % Set seed for reproducible results
randomNoise1 = rand(1, length(t1));

% Generate the wave signal with noise
wave1 = (amplitude1/CONFIG1.amplitudeScale) .* cos(2 * pi * COMMON.frequency * t1) + ...
        randomNoise1 * CONFIG1.noiseLevel;

%% GENERATE CONFIGURATION 2: PROPERLY SAMPLED WAVE WITHOUT NOISE
fprintf('Generating Configuration 2: Clean decaying wave...\n');

% Time vector for configuration 2
t2 = 1:CONFIG2.samplingRate:COMMON.duration;

% Calculate amplitude with exponential decay
amplitude2 = exp(-CONFIG2.decayRate * t2);

% Generate the clean wave signal (no noise)
wave2 = amplitude2 .* cos(2 * pi * COMMON.frequency * t2);

%% VISUALIZATION
fprintf('Creating plots...\n');

% Create figure with subplots for comparison
figure('Position', [100, 100, 1200, 500], 'Name', 'Wave Generation Analysis');

% Subplot 1: Undersampled wave with noise
subplot(1, 2, 1);
plot(t1, wave1, 'b-', 'LineWidth', 1.5);
title('Configuration 1: Undersampled Wave with Noise', 'FontSize', 12, 'FontWeight', 'bold');
xlabel('Time (s)', 'FontSize', 10);
ylabel('Amplitude', 'FontSize', 10);
grid on;
xlim([0, COMMON.duration]);
legend('Wave + Noise', 'Location', 'northeast');

% Add annotation about sampling rate
text(0.05, 0.95, sprintf('Sampling Rate: %.1f Hz', CONFIG1.samplingRate), ...
     'Units', 'normalized', 'FontSize', 9, 'BackgroundColor', 'white');

% Subplot 2: Clean decaying wave
subplot(1, 2, 2);
plot(t2, wave2, 'r-', 'LineWidth', 1.5);
title('Configuration 2: Clean Decaying Wave', 'FontSize', 12, 'FontWeight', 'bold');
xlabel('Time (s)', 'FontSize', 10);
ylabel('Amplitude', 'FontSize', 10);
grid on;
xlim([1, COMMON.duration]);
legend('Clean Wave', 'Location', 'northeast');

% Add annotation about sampling rate
text(0.05, 0.95, sprintf('Sampling Rate: %.1f Hz', CONFIG2.samplingRate), ...
     'Units', 'normalized', 'FontSize', 9, 'BackgroundColor', 'white');

%% DATA ANALYSIS (Optional)
fprintf('Performing basic analysis...\n');

% Display summary statistics
fprintf('\n=== WAVE ANALYSIS SUMMARY ===\n');
fprintf('Configuration 1:\n');
fprintf('  - Number of samples: %d\n', length(wave1));
fprintf('  - Sampling period: %.3f s\n', 1/CONFIG1.samplingRate);
fprintf('  - Final amplitude: %.4f\n', wave1(end));

fprintf('Configuration 2:\n');
fprintf('  - Number of samples: %d\n', length(wave2));
fprintf('  - Sampling period: %.3f s\n', 1/CONFIG2.samplingRate);
fprintf('  - Final amplitude: %.4f\n', wave2(end));

fprintf('\nAnalysis complete. Figures displayed.\n');

%% SAVE RESULTS (Optional)
% Uncomment the following lines to save the results:
% save('wave_data.mat', 't1', 'wave1', 't2', 'wave2', 'COMMON', 'CONFIG1', 'CONFIG2');
% fprintf('Data saved to wave_data.mat\n');