#include <vector>
#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

bool compare(int x, int y) {
  return y < x;
}

int main() {
  int n;
  int x;
  cin >> n;
  vector<int> maxHeap; // first half
  vector<int> minHeap; // second half
  double median = 0;

  for (int i = 0; i < n; i++) {
    cin >> x;
    if (i == 0 || x <= median) {
      maxHeap.push_back(x);
      push_heap(maxHeap.begin(), maxHeap.end());
    } else {
      minHeap.push_back(x);
      push_heap(minHeap.begin(), minHeap.end(), compare);
    }

    if (maxHeap.size() > minHeap.size() + 1) {
      x = maxHeap[0];
      pop_heap(maxHeap.begin(), maxHeap.end());
      maxHeap.pop_back();
      minHeap.push_back(x);
      push_heap(minHeap.begin(), minHeap.end(), compare);
    }

    if (minHeap.size() > maxHeap.size() + 1) {
      x = minHeap[0];
      pop_heap(minHeap.begin(), minHeap.end(), compare);
      minHeap.pop_back();
      maxHeap.push_back(x);
      push_heap(maxHeap.begin(), maxHeap.end());
    }

    if (maxHeap.size() > minHeap.size()) {
      median = maxHeap[0];
    } else if (maxHeap.size() < minHeap.size()) {
      median = minHeap[0];
    } else {
      median = (minHeap[0] + maxHeap[0]) / 2.0;
    }
    printf("%.1f\n", median);
  }
  return 0;
}
