#include <iostream>
#include <vector>
#include <utility>
#include <queue>
using namespace std;
pair<int, int> arrow[4] = { make_pair(1,0),make_pair(-1,0),make_pair(0,1),make_pair(0,-1) };
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
bool check(int x, int y, int n, int m) {
   return (x >= 0 && x < m) && (y >= 0 && y < n);
}
int main() {
   int m = 0, n = 0;
   int Tcase, cnt;
   int x, y, nx, ny;
   
   scanf("%d", &Tcase);
   for (int i = 0; i < Tcase; i++) {
      scanf("%d %d %d", &m, &n, &cnt);
      vector<vector<int> > arr(m, vector<int>(n, 0));
      vector<int> ans;
      for (int j = 0; j < cnt; j++) {
         scanf("%d %d", &x, &y);
         arr[x][y] = 1;
      }
      
      for (int k = 0; k < arr.size(); k++) {
         for (int w = 0; w < arr[k].size(); w++) {
            if (arr[k][w] == 1) {
               pair<int, int> xy;
               queue<pair<int, int> > q;
               q.push(make_pair(k, w));
               int index = 0;
               while (!q.empty()) {
                  xy = q.front();
                  x = xy.first;
                  y = xy.second;
                  q.pop();
                  for (int e = 0; e < 4; e++) {
                     nx = x + arrow[e].first;
                     ny = y + arrow[e].second;
                     if (check(nx, ny, n, m) && arr[nx][ny] == 1) {
                        arr[nx][ny] = 0;
                        q.push(make_pair(nx, ny));
                        index += 1;
                     }
                  }

               }
               ans.push_back(index);
            }
         }
      }
      printf("%d\n", ans.size());

   }
   return 0;
}