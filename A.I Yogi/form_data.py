import json,time
#from camera import VideoCamera
from flask import Flask, render_template, request, jsonify, Response
import requests
import base64,cv2
from imutils.video import WebcamVideoStream
from playsound import playsound

import mediapipe as mp
import numpy as np
import time
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

app = Flask(__name__, template_folder='template')
output=[]#("message stark","hi")]
@app.route('/')
def home_page():
    return render_template("MY_Home_page.html",result=output)

@app.route('/selection')
def selection():
    return render_template("selection.html",result=output)

def gen():
    video = cv2.VideoCapture(0)
    vrukshasana = [0.5042802691459656,
 0.28603190183639526,
 0.5127906799316406,
 0.269010066986084,
 0.5182839632034302,
 0.26899775862693787,
 0.5229371786117554,
 0.26896774768829346,
 0.49710607528686523,
 0.2698418200016022,
 0.4917624890804291,
 0.2708059251308441,
 0.4874544143676758,
 0.27170589566230774,
 0.5293115973472595,
 0.2767108380794525,
 0.4839872717857361,
 0.28288063406944275,
 0.5147734880447388,
 0.3035500645637512,
 0.49518021941185,
 0.30649518966674805,
 0.5721458792686462,
 0.36043494939804077,
 0.44962987303733826,
 0.36866721510887146,
 0.6151943802833557,
 0.2281818985939026,
 0.39268776774406433,
 0.24649932980537415,
 0.5213020443916321,
 0.16434521973133087,
 0.47410568594932556,
 0.16159267723560333,
 0.5061672925949097,
 0.14365318417549133,
 0.48756495118141174,
 0.1361221969127655,
 0.5000219345092773,
 0.14637623727321625,
 0.49328964948654175,
 0.14120784401893616,
 0.5029188394546509,
 0.15919961035251617,
 0.4923909604549408,
 0.15579639375209808,
 0.5545766949653625,
 0.6675569415092468,
 0.47255292534828186,
 0.6649314165115356,
 0.5352116823196411,
 0.8883389234542847,
 0.35864853858947754,
 0.7897482514381409,
 0.5216404795646667,
 0.9576961398124695,
 0.5059784650802612,
 0.7799226641654968,
 0.518074631690979,
 0.969854474067688,
 0.5207595825195312,
 0.763558030128479,
 0.5260140895843506,
 1.020667314529419,
 0.5350929498672485,
 0.8737634420394897]
            
## Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
       
            c=0
            
            while(True):
                
                    c = c+1
            #v = time.time()
                    posess = []
                    rate, image = video.read()
        # Recolor image to RGB
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    image.flags.writeable = False
      
        # Make detection
                    results = pose.process(image)
    
        # Recolor back to BGR
                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                #g = time.time()
        # Extract landmarks
                
            
                
                    landmarks = results.pose_landmarks.landmark
                    print(landmarks)
                    for lndmrk in mp_pose.PoseLandmark:
                        j = landmarks[lndmrk.value].x
                        posess.append(j)
                        k = landmarks[lndmrk.value].y
                        posess.append(k)
               
            
        
        
        # Render detections
                    
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                )         
                   
                    vrukshasana = np.array(vrukshasana)
                    posess = np.array(posess)
                    name = ''
                    dist = np.linalg.norm(vrukshasana-posess)
                    if(dist == 0):
                            name = 'exelent'
                            cv2.putText(image, name, (45, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                        
                    if(dist < 1.00):
                            name = 'good'
                            cv2.putText(image, name, (45 , 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                       
                    if(dist > 1.50):
                            name = 'bad'
                            cv2.putText(image, name, (45, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                           
                    ret, jpg = cv2.imencode('.jpg', image)
                    data = []
                    data.append(jpg.tobytes())
                    data.append(name)
        #data= camera.get_frame()

                    frame=data[0]
                    yield (b'--frame\r\n'
                            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def gen1():
    tadasana = [0.4972565770149231,
 0.3451427221298218,
 0.5040279626846313,
 0.3260895609855652,
 0.5087680220603943,
 0.324612021446228,
 0.5132666826248169,
 0.3231705129146576,
 0.4887252449989319,
 0.3291390538215637,
 0.48388758301734924,
 0.3298121392726898,
 0.47888484597206116,
 0.33050668239593506,
 0.5185537338256836,
 0.3243275284767151,
 0.47437649965286255,
 0.33651888370513916,
 0.5081908702850342,
 0.35813063383102417,
 0.4894956648349762,
 0.3618085980415344,
 0.5519770979881287,
 0.38671886920928955,
 0.45118218660354614,
 0.39607149362564087,
 0.5634192824363708,
 0.2511076331138611,
 0.4248594641685486,
 0.2723577320575714,
 0.5365902185440063,
 0.14057080447673798,
 0.4554535448551178,
 0.15197177231311798,
 0.5243546366691589,
 0.11587963253259659,
 0.4669617712497711,
 0.12510517239570618,
 0.5192586183547974,
 0.11496666818857193,
 0.47394227981567383,
 0.1213301420211792,
 0.5201883316040039,
 0.12437856942415237,
 0.4741027355194092,
 0.13046075403690338,
 0.537910521030426,
 0.6646974086761475,
 0.4723081588745117,
 0.6646918058395386,
 0.5304211378097534,
 0.8621702790260315,
 0.4708959460258484,
 0.8593955636024475,
 0.5170029401779175,
 1.0073106288909912,
 0.4763471186161041,
 1.0090807676315308,
 0.5128369927406311,
 1.0288658142089844,
 0.47810572385787964,
 1.0268685817718506,
 0.5129908323287964,
 1.0751465559005737,
 0.4718242585659027,
 1.0878349542617798]
    video = cv2.VideoCapture(0)
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
       
            c=0
            
            while(True):
                
                    c = c+1
            #v = time.time()
                    posess = []
                    rate, image = video.read()
        # Recolor image to RGB
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    image.flags.writeable = False
      
        # Make detection
                    results = pose.process(image)
    
        # Recolor back to BGR
                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                #g = time.time()
        # Extract landmarks
                
            
                
                    landmarks = results.pose_landmarks.landmark
                    print(landmarks)
                    for lndmrk in mp_pose.PoseLandmark:
                        j = landmarks[lndmrk.value].x
                        posess.append(j)
                        k = landmarks[lndmrk.value].y
                        posess.append(k)
               
            
        
        
        # Render detections
                    
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                )         
                   
                    tadasana = np.array(tadasana)
                    posess = np.array(posess)
                    name = ''
                    dist = np.linalg.norm(tadasana-posess)
                    if(dist == 0):
                            name = 'exelent'
                            cv2.putText(image, name, (45, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                            
                    if(dist < 1.00):
                            name = 'good'
                            cv2.putText(image, name, (45 , 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                          
                    if(dist > 1.50):
                            name = 'bad'
                            cv2.putText(image, name, (45, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                          
                    ret, jpg = cv2.imencode('.jpg', image)
                    data = []
                    data.append(jpg.tobytes())
                    data.append(name)
        #data= camera.get_frame()

                    frame=data[0]
                    yield (b'--frame\r\n'
                            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        

def gen2():
    parvatasana = [0.7304171919822693,
 0.644785463809967,
 0.7275189161300659,
 0.6638696193695068,
 0.7261379361152649,
 0.6639311909675598,
 0.7251832485198975,
 0.663696825504303,
 0.729710578918457,
 0.6590899229049683,
 0.7263588905334473,
 0.6584725975990295,
 0.7157987356185913,
 0.649382472038269,
 0.7139877080917358,
 0.6596785187721252,
 0.7012864351272583,
 0.6355032324790955,
 0.7141937613487244,
 0.6288236379623413,
 0.7202938199043274,
 0.6196520328521729,
 0.6889127492904663,
 0.5948893427848816,
 0.6549097299575806,
 0.5714650750160217,
 0.791365921497345,
 0.7094547748565674,
 0.7307522296905518,
 0.6614530682563782,
 0.8426858186721802,
 0.828288197517395,
 0.820395290851593,
 0.762438952922821,
 0.8501079678535461,
 0.854059100151062,
 0.8239304423332214,
 0.7822816371917725,
 0.8450568318367004,
 0.8533068299293518,
 0.8440338969230652,
 0.774713933467865,
 0.8420252799987793,
 0.842992901802063,
 0.8418607711791992,
 0.7726951837539673,
 0.480243057012558,
 0.3715149164199829,
 0.4490092694759369,
 0.36045461893081665,
 0.33503231406211853,
 0.607504665851593,
 0.30347734689712524,
 0.6096563339233398,
 0.2801801264286041,
 0.8351904153823853,
 0.26702433824539185,
 0.8434469699859619,
 0.26592642068862915,
 0.895359456539154,
 0.2572154700756073,
 0.9114720821380615,
 0.24393649399280548,
 0.8879916071891785,
 0.22806434333324432,
 0.8956025838851929]
    video = cv2.VideoCapture(0)
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
       
            c=0
            
            while(True):
                
                    c = c+1
            #v = time.time()
                    posess = []
                    rate, image = video.read()
        # Recolor image to RGB
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    image.flags.writeable = False
      
        # Make detection
                    results = pose.process(image)
    
        # Recolor back to BGR
                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                #g = time.time()
        # Extract landmarks
                
            
                
                    landmarks = results.pose_landmarks.landmark
                    print(landmarks)
                    for lndmrk in mp_pose.PoseLandmark:
                        j = landmarks[lndmrk.value].x
                        posess.append(j)
                        k = landmarks[lndmrk.value].y
                        posess.append(k)
               
            
        
        
        # Render detections
                    
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                )         
                   
                    parvatasana = np.array(parvatasana)
                    posess = np.array(posess)
                    name = ''
                    dist = np.linalg.norm(parvatasana-posess)
                    if(dist == 0):
                            name = 'exelent'
                            cv2.putText(image, name, (45, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                           
                    if(dist < 1.00):
                            name = 'good'
                            cv2.putText(image, name, (45 , 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                            
                    if(dist > 1.50):
                            name = 'bad'
                            cv2.putText(image, name, (45, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                            
                    ret, jpg = cv2.imencode('.jpg', image)
                    data = []
                    data.append(jpg.tobytes())
                    data.append(name)
        #data= camera.get_frame()

                    frame=data[0]
                    yield (b'--frame\r\n'
                            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def gen3():
    sarvangasana = [0.1646987497806549,
 0.700744092464447,
 0.13930867612361908,
 0.7073414325714111,
 0.13831853866577148,
 0.7074170708656311,
 0.13716252148151398,
 0.707846999168396,
 0.14012907445430756,
 0.7171784043312073,
 0.14022786915302277,
 0.7246319055557251,
 0.1405474990606308,
 0.7320103049278259,
 0.14023439586162567,
 0.7395433783531189,
 0.14416661858558655,
 0.7725722789764404,
 0.18186578154563904,
 0.7142238020896912,
 0.18272657692432404,
 0.7274720072746277,
 0.2185813933610916,
 0.7566354870796204,
 0.25609031319618225,
 0.8505612015724182,
 0.32419997453689575,
 0.6968516707420349,
 0.4476219713687897,
 0.8966982364654541,
 0.3405380845069885,
 0.6069275140762329,
 0.43351712822914124,
 0.6649666428565979,
 0.3516685366630554,
 0.5871689915657043,
 0.43896690011024475,
 0.6123178005218506,
 0.34214121103286743,
 0.5752764344215393,
 0.4242152273654938,
 0.5997529625892639,
 0.337322860956192,
 0.5971943140029907,
 0.4185773730278015,
 0.6178049445152283,
 0.43184494972229004,
 0.661611795425415,
 0.47431808710098267,
 0.7149772047996521,
 0.4926278591156006,
 0.49464812874794006,
 0.5520997047424316,
 0.5166941285133362,
 0.5815168023109436,
 0.4093531668186188,
 0.6318607926368713,
 0.42925792932510376,
 0.6029088497161865,
 0.41266921162605286,
 0.6508009433746338,
 0.4293166399002075,
 0.6029955744743347,
 0.3323403000831604,
 0.6442970633506775,
 0.35592660307884216]
    video = cv2.VideoCapture(0)
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
       
            c=0
            
            while(True):
                
                    c = c+1
            #v = time.time()
                    posess = []
                    rate, image = video.read()
        # Recolor image to RGB
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    image.flags.writeable = False
      
        # Make detection
                    results = pose.process(image)
    
        # Recolor back to BGR
                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                #g = time.time()
        # Extract landmarks
                
            
                
                    landmarks = results.pose_landmarks.landmark
                    print(landmarks)
                    for lndmrk in mp_pose.PoseLandmark:
                        j = landmarks[lndmrk.value].x
                        posess.append(j)
                        k = landmarks[lndmrk.value].y
                        posess.append(k)
               
            
        
        
        # Render detections
                    
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                )         
                   
                    sarvangasana = np.array(sarvangasana)
                    posess = np.array(posess)
                    name = ''
                    dist = np.linalg.norm(sarvangasana-posess)
                    if(dist == 0):
                            name = 'exelent'
                            cv2.putText(image, name, (45, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                           
                    if(dist < 1.00):
                            name = 'good'
                            cv2.putText(image, name, (45 , 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                            
                    if(dist > 1.50):
                            name = 'bad'
                            cv2.putText(image, name, (45, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                            
                    ret, jpg = cv2.imencode('.jpg', image)
                    data = []
                    data.append(jpg.tobytes())
                    data.append(name)
        #data= camera.get_frame()

                    frame=data[0]
                    yield (b'--frame\r\n'
                            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def gen4():
    dhanurasana = [0.9496876001358032,
 0.6529626846313477,
 0.9513999223709106,
 0.600791335105896,
 0.9485486745834351,
 0.5967333316802979,
 0.9452759027481079,
 0.5921918153762817,
 0.9481486082077026,
 0.6020896434783936,
 0.9433870315551758,
 0.5992054343223572,
 0.9384959936141968,
 0.596522331237793,
 0.9056892395019531,
 0.5775089859962463,
 0.8975159525871277,
 0.5847465991973877,
 0.9206473231315613,
 0.6705829501152039,
 0.9189894795417786,
 0.6716433167457581,
 0.7358914017677307,
 0.5968406200408936,
 0.7543362379074097,
 0.6402391195297241,
 0.5339025855064392,
 0.4167904853820801,
 0.5326720476150513,
 0.4109093248844147,
 0.3538673222064972,
 0.24609842896461487,
 0.3279004693031311,
 0.24132147431373596,
 0.29341214895248413,
 0.18695242702960968,
 0.28347525000572205,
 0.19263461232185364,
 0.2966803014278412,
 0.1863676756620407,
 0.27872705459594727,
 0.19488024711608887,
 0.3076730966567993,
 0.2026054412126541,
 0.2910676598548889,
 0.21533089876174927,
 0.31849372386932373,
 0.7471517324447632,
 0.2984561622142792,
 0.7683588266372681,
 0.0552482008934021,
 0.671521008014679,
 -0.0007496460457332432,
 0.6909297108650208,
 0.11453185975551605,
 0.3571838438510895,
 0.06977002322673798,
 0.3444293141365051,
 0.14742040634155273,
 0.30557456612586975,
 0.14196184277534485,
 0.30222731828689575,
 -0.013373489491641521,
 0.31248390674591064,
 -0.04127124324440956,
 0.3116704523563385]
    video = cv2.VideoCapture(0)
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
       
            c=0
            
            while(True):
                
                    c = c+1
            #v = time.time()
                    posess = []
                    rate, image = video.read()
        # Recolor image to RGB
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    image.flags.writeable = False
      
        # Make detection
                    results = pose.process(image)
    
        # Recolor back to BGR
                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                #g = time.time()
        # Extract landmarks
                
            
                
                    landmarks = results.pose_landmarks.landmark
                    print(landmarks)
                    for lndmrk in mp_pose.PoseLandmark:
                        j = landmarks[lndmrk.value].x
                        posess.append(j)
                        k = landmarks[lndmrk.value].y
                        posess.append(k)
               
            
        
        
        # Render detections
                    
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                )         
                   
                    dhanurasana = np.array(dhanurasana)
                    posess = np.array(posess)
                    name = ''
                    dist = np.linalg.norm(dhanurasana-posess)
                    if(dist == 0):
                            name = 'exelent'
                            cv2.putText(image, name, (45, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                           
                    if(dist < 1.00):
                            name = 'good'
                            cv2.putText(image, name, (45 , 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                            
                    if(dist > 1.50):
                            name = 'bad'
                            cv2.putText(image, name, (45, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                            
                    ret, jpg = cv2.imencode('.jpg', image)
                    data = []
                    data.append(jpg.tobytes())
                    data.append(name)
        #data= camera.get_frame()

                    frame=data[0]
                    yield (b'--frame\r\n'
                            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def gen5():
    ushtrasana = [0.2139473855495453,
 0.2838287055492401,
 0.20534846186637878,
 0.24873876571655273,
 0.20637166500091553,
 0.23603159189224243,
 0.20636990666389465,
 0.23439067602157593,
 0.20234861969947815,
 0.24206160008907318,
 0.2028866559267044,
 0.2385730892419815,
 0.2025298774242401,
 0.2363155335187912,
 0.22444216907024384,
 0.2173498570919037,
 0.217980295419693,
 0.21915759146213531,
 0.2414574921131134,
 0.2819215953350067,
 0.23800328373908997,
 0.29033568501472473,
 0.3303323984146118,
 0.2854977548122406,
 0.29673734307289124,
 0.27659276127815247,
 0.307662695646286,
 0.5795247554779053,
 0.29769498109817505,
 0.504330039024353,
 0.25576257705688477,
 0.8091237545013428,
 0.26512500643730164,
 0.7712552547454834,
 0.24288158118724823,
 0.8703140616416931,
 0.2486284077167511,
 0.8157461285591125,
 0.2365114390850067,
 0.8668497800827026,
 0.2456474006175995,
 0.8339211940765381,
 0.2432795763015747,
 0.8492158651351929,
 0.25579744577407837,
 0.8182928562164307,
 0.5797240138053894,
 0.6591647863388062,
 0.5326459407806396,
 0.654051661491394,
 0.6201130151748657,
 0.992477297782898,
 0.6019290685653687,
 0.9619342684745789,
 0.6885133981704712,
 1.2192623615264893,
 0.6555017828941345,
 1.1893858909606934,
 0.7119694948196411,
 1.2280700206756592,
 0.6814025640487671,
 1.208077073097229,
 0.6653943657875061,
 1.3311525583267212,
 0.6179276704788208,
 1.3011521100997925]
    video = cv2.VideoCapture(0)
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
       
            c=0
            
            while(True):
                
                    c = c+1
            #v = time.time()
                    posess = []
                    rate, image = video.read()
        # Recolor image to RGB
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    image.flags.writeable = False
      
        # Make detection
                    results = pose.process(image)
    
        # Recolor back to BGR
                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                #g = time.time()
        # Extract landmarks
                
            
                
                    landmarks = results.pose_landmarks.landmark
                    print(landmarks)
                    for lndmrk in mp_pose.PoseLandmark:
                        j = landmarks[lndmrk.value].x
                        posess.append(j)
                        k = landmarks[lndmrk.value].y
                        posess.append(k)
               
            
        
        
        # Render detections
                    
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                )         
                   
                    ushtrasana = np.array(ushtrasana)
                    posess = np.array(posess)
                    name = ''
                    dist = np.linalg.norm(ushtrasana-posess)
                    if(dist == 0):
                            name = 'exelent'
                            cv2.putText(image, name, (45, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                           
                    if(dist < 1.00):
                            name = 'good'
                            cv2.putText(image, name, (45 , 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                            
                    if(dist > 1.50):
                            name = 'bad'
                            cv2.putText(image, name, (45, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                            
                    ret, jpg = cv2.imencode('.jpg', image)
                    data = []
                    data.append(jpg.tobytes())
                    data.append(name)
        #data= camera.get_frame()

                    frame=data[0]
                    yield (b'--frame\r\n'
                            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def gen6():
    bhujangasana = [0.7758035659790039,
 0.03769674524664879,
 0.7508295178413391,
 0.029159100726246834,
 0.7481298446655273,
 0.03256699815392494,
 0.744800329208374,
 0.03565656393766403,
 0.7490739226341248,
 0.03233490511775017,
 0.7462583780288696,
 0.037144340574741364,
 0.7435141801834106,
 0.04125935211777687,
 0.7227295637130737,
 0.07704667747020721,
 0.7249829769134521,
 0.08444951474666595,
 0.7816880941390991,
 0.07901067286729813,
 0.7781715989112854,
 0.08135756105184555,
 0.695839524269104,
 0.25862815976142883,
 0.7261584997177124,
 0.27882376313209534,
 0.6630505323410034,
 0.5603259801864624,
 0.6876387596130371,
 0.601554274559021,
 0.7093633413314819,
 0.8310148119926453,
 0.7687245011329651,
 0.9264470934867859,
 0.7460558414459229,
 0.8323606252670288,
 0.8229736089706421,
 0.9392825961112976,
 0.7606925368309021,
 0.8382812142372131,
 0.8352266550064087,
 0.9248397350311279,
 0.7397688627243042,
 0.8495022654533386,
 0.8175634145736694,
 0.9230391383171082,
 0.468798965215683,
 0.7136937975883484,
 0.47343286871910095,
 0.7567982077598572,
 0.15854774415493011,
 0.8029840588569641,
 0.14732755720615387,
 0.844358503818512,
 -0.11409975588321686,
 0.7921168804168701,
 -0.12689253687858582,
 0.8360892534255981,
 -0.1642461121082306,
 0.7466239929199219,
 -0.17293287813663483,
 0.8172065615653992,
 -0.1699434369802475,
 0.8553580045700073,
 -0.19457635283470154,
 0.8391780853271484]
    video = cv2.VideoCapture(0)
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
       
            c=0
            
            while(True):
                
                    c = c+1
            #v = time.time()
                    posess = []
                    rate, image = video.read()
        # Recolor image to RGB
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    image.flags.writeable = False
      
        # Make detection
                    results = pose.process(image)
    
        # Recolor back to BGR
                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                #g = time.time()
        # Extract landmarks
                
            
                
                    landmarks = results.pose_landmarks.landmark
                    print(landmarks)
                    for lndmrk in mp_pose.PoseLandmark:
                        j = landmarks[lndmrk.value].x
                        posess.append(j)
                        k = landmarks[lndmrk.value].y
                        posess.append(k)
               
            
        
        
        # Render detections
                    
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                )         
                   
                    bhujangasana = np.array(bhujangasana)
                    posess = np.array(posess)
                    name = ''
                    dist = np.linalg.norm(bhujangasana-posess)
                    if(dist == 0):
                            name = 'exelent'
                            cv2.putText(image, name, (45, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                           
                    if(dist < 1.00):
                            name = 'good'
                            cv2.putText(image, name, (45 , 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                            
                    if(dist > 1.50):
                            name = 'bad'
                            cv2.putText(image, name, (45, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                            
                    ret, jpg = cv2.imencode('.jpg', image)
                    data = []
                    data.append(jpg.tobytes())
                    data.append(name)
        #data= camera.get_frame()

                    frame=data[0]
                    yield (b'--frame\r\n'
                            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



@app.route('/vrukshasana')
def vrukshasana():
    return render_template("vrukshasana.html",result=output)

@app.route('/tadasana')
def tadasana():
    return render_template("tadasana.html",result=output)

@app.route('/parvatasana')
def parvatasana():
    return render_template("parvatasana.html",result=output)

@app.route('/sarvangasana')
def sarvangasana():
    return render_template("sarvangasana.html",result=output)

@app.route('/dhanurasana')
def dhanurasana():
    return render_template("dhanurasana.html",result=output)

@app.route('/ushtrasana')
def ushtrasana():
    return render_template("ushtrasana.html",result=output)

@app.route('/bhujangasana')
def bhujangasana():
    return render_template("bhujangasana.html",result=output)






@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed1')
def video_feed1():
    return Response(gen1(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed2')
def video_feed2():
    return Response(gen2(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed3')
def video_feed3():
    return Response(gen3(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed4')
def video_feed4():
    return Response(gen4(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed5')
def video_feed5():
    return Response(gen5(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed6')
def video_feed6():
    return Response(gen6(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__=="__main__":
    app.run(debug=True)#,host="192.168.43.161")
