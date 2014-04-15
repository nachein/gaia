var MockAttentionScreen = {
  attentionScreen: document.createElement('div'),
  open: function() {},
  mVisible: false,
  mFullyVisible: false,
  isVisible: function() {
    return this.mVisible;
  },
  isFullyVisible: function() {
    return this.mFullyVisible;
  },
  mTeardown: function() {
    this.mVisible = false;
    this.mFullyVisible = false;
  }
};
