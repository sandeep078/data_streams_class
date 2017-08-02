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
  for (int i = 0; i < states.length; ++i) {
    colorState(states[i],color(0,colors[i],0));
  }
}

}

</script>
<canvas id="pjs"></canvas>
</body>
</html>
