function varargout = ADC_GUI(varargin)
% ADC_GUI MATLAB code for ADC_GUI.fig
%      CLASS_5_ADC_GUI, by itself, creates a new CLASS_5_ADC_GUI or raises the existing
%      singleton*.
%
%      H = ADC_GUI returns the handle to a new CLASS_5_ADC_GUI or the handle to
%      the existing singleton*.
%
%      ADC_GUI('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in CLASS_5_ADC_GUI.M with the given input arguments.
%
%      ADC_GUI('Property','Value',...) creates a new CLASS_5_ADC_GUI or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before Class_5_ADC_GUI_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to Class_5_ADC_GUI_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help Class_5_ADC_GUI

% Last Modified by GUIDE v2.5 15-Sep-2013 17:57:30
%
% Based on examples used in Fun with Arduino by Rob Purser
%
%Fun with Raspberry Pi by Brian Bodiya & Tom Amlicke is licensed under a
%Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
%Based on a work at https://github.com/bodiya/funwithraspberrypi.
%
%Copyright Brian Bodiya & Tom Amlicke, 2014

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @ADC_GUI_OpeningFcn, ...
                   'gui_OutputFcn',  @ADC_GUI_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before Class_5_FSR_GUI is made visible.
function ADC_GUI_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to Class_5_ADC_GUI (see VARARGIN)

% Choose default command line output for Class_5_ADC_GUI
handles.output = hObject;

% Clear all previously created objects
clear rpi;
clear adc;

% Create initial plot
plot(handles.axesHandle,0,0,'MarkerFaceColor','auto','MarkerEdgeColor',[0 1 0],'Marker','.','LineWidth',1,'Color',[0 1 0]);

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes Class_5_ADC_GUI wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = ADC_GUI_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in startButton.
function startButton_Callback(hObject, eventdata, handles)
% hObject    handle to startButton (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

button_state = get(hObject,'Value');
if button_state == get(hObject,'Max')
	% Toggle button is pressed
    
    % Change the string on the button
    set(hObject,'String','Stop');
    
    % Check if the object is already created
    if ~exist('adc','var')
        % Create an object to connect to Raspberry Pi board
        rpi = raspi();
        adc = i2cdev(rpi, 'i2c-1', hex2dec('48'));
        
        % Reset data array
        clear data;
        % Reset initial plot
        plot(handles.axesHandle,0,0,'MarkerFaceColor','auto','MarkerEdgeColor',[0 1 0],'Marker','.','LineWidth',1,'Color',[0 1 0]);

    end
    
elseif button_state == get(hObject,'Min')
	% Toggle button is not pressed
    
    % Change the string on the button
    set(hObject,'String','Start');
    
    % Clear the object created
    clear a;
end

tic;
iLoop = 1;
while isequal(get(hObject,'Value'),get(hObject,'Max'))
    data(iLoop) = read(adc,1);  %#ok<*AGROW>
    timeStamp(iLoop) = toc; 
    plot(handles.axesHandle,timeStamp,data,'MarkerFaceColor','auto','MarkerEdgeColor',[0 1 0],'Marker','.','LineWidth',1,'Color',[0 1 0]);
    iLoop = iLoop+1;
    drawnow;
end



