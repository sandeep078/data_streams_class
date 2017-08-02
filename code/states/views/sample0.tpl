<html>
<head>
<title>Map demo page</title>
<script src="/static/processing.min.js"></script>
</head>
<body>
<script type="application/processing" data-processing-target="pjs">

void setup() {
  background(255);
  size(950, 600);
  usa = loadShape("/static/Simple_US_Map.svg");
  noLoop();
  smooth(); // Improves the drawing quality of the SVG
}

void color_state(s,c) {
    state = usa.getChild(s);
    state.disableStyle();
    fill(c);
    noStroke();
    shape(state,0,0);
}

void draw() {
  shape(usa,0,0);
  for (int i = 0; i < states.length; i++) {
    color_state(states[i],color(reds[i],greens[i],blues[i]));
  }
}

</script>
<canvas id="pjs"></canvas>
</body>
</html>
