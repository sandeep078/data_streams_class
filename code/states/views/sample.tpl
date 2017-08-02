<html>
<head>
<title>Map demo page</title>
<script src="/static/processing.min.js"></script>
</head>
<body>
<div>{{states}}</div>
<div>{{colors}}</div>
<script type="application/processing" data-processing-target="pjs">
String [] states = { {{!states}} };
int [] colors = { {{!colors}} };

String [] Obama  = { "HI", "RI", "CT", "MA", "ME", "NH", "VT", "NY", "NJ",
     "FL", "NC", "OH", "IN", "IA", "CO", "NV", "PA", "DE", "MD", "MI",
     "WA", "CA", "OR", "IL", "MN", "WI", "DC", "NM", "VA" };

String [] McCain = { "AK", "GA", "AL", "TN", "WV", "KY", "SC", "WY", "MT",
     "ID", "TX", "AZ", "UT", "ND", "SD", "NE", "MS", "MO", "AR", "OK",
     "KS", "LA" };

void setup() {
  background(255);
  size(950, 600);
  usa = loadShape("/static/Simple_US_Map.svg");
  noLoop();
  smooth(); // Improves the drawing quality of the SVG
}

void colorState(state,c) {
  border = usa.getChild(state);
  border.disableStyle();
  fill(c);
  noStroke();
  shape(border,0,0)
}

void draw() {
  shape(usa,0,0);
  statesColoring(Obama , color(0, 0, 255));
  statesColoring(McCain, color(255, 0, 0));
  for (int i = 0; i < states.length; ++i) {
    colorState(states[i],color(0,colors[i],0));
  }
  //println('hello web!');
  //println(states);
  //println(colors);
}

void statesColoring(String[] states, int c){
  for (int i = 0; i < states.length; ++i) {
    state = usa.getChild(states[i]);
    // Disable the colors found in the SVG file
    // state.disableStyle();
    // Set our own coloring
    fill(c);
    noStroke();
    // Draw a single state
    shape(state, 0, 0);
  }
}

</script>
<canvas id="pjs"></canvas>
</body>
</html>
