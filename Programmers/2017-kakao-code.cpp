#include <vector>
#include <queue>
using namespace std;
pair<int, int> arrow[4] = { make_pair(1,0),make_pair(-1,0),make_pair(0,1),make_pair(0,-1) };
bool check(int x, int y, int n, int m) {
   return (x >= 0 && x < m) && (y >= 0 && y < n);
}
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    int x, y;
    vector<int> tmp;
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
         if (picture[i][j] != 0) {
            pair<int, int> xy;
            int index = 0;
            int cur = picture[i][j];
            queue<pair<int, int> > q;
            q.push(make_pair(i, j));
            while (!q.empty()) {
               xy = q.front();
               x = xy.first;
               y = xy.second;
               q.pop();
               for (int w = 0; w < 4; w++) {
                  int nx = x + arrow[w].first;
                  int ny = y + arrow[w].second;
                  if (check(nx, ny,n,m) && picture[nx][ny] != 0 && cur == picture[nx][ny]) {
                     index += 1;
                     picture[nx][ny] = 0;
                     q.push(make_pair(nx, ny));
                     
                  }
               }
            }
            tmp.push_back(index);
         }
      }
   }
    vector<int> answer(2);
    answer[0] = tmp.size();
    for (auto i : tmp) {
      answer[1] = max(answer[1],i);
   }
    
    return answer;
}