import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { map, catchError } from 'rxjs/operators';

import { Observable, throwError } from 'rxjs';
import { VideoInfo } from '../youtube/video-info-module';
import { YOUTUBE_API_FEATURE } from '../env';
import { YOUTUBE_API_URL } from '../env';
import { YOUTUBE_API_KEY } from '../env';
import { API_URL } from '../env';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json'
  })
};

@Injectable({
  providedIn: 'root'
})

export class YoutubeSearchService {



  constructor(private http: HttpClient) { }

  search(query: string): Observable<VideoInfo[]> {
    const params: string = [
      `part=snippet`,
      `maxResults=25`,
      `q=${query}`,
      `type=video`,
      `key=${YOUTUBE_API_KEY}`
    ].join('&');

    const queryUrl = `${YOUTUBE_API_URL}${YOUTUBE_API_FEATURE[0]}?${params}`;

    return this.http.get(queryUrl).pipe(map(response => {
      return response['items'].map(item => {
        return new VideoInfo({
          id: item.id.videoId,
          title: item.snippet.title,
          description: item.snippet.description,
          thumbnailUrl: item.snippet.thumbnails.high.url
        });
      });
    }));
  }

  saveVideoComments(videoId: string) {
    const options = {headers: {'Content-Type':  'application/json'}};
    var data = {"videoId": videoId, "key": YOUTUBE_API_KEY, "url": YOUTUBE_API_URL, "feature": YOUTUBE_API_FEATURE[1]};
    this.http.post<JSON>(`${API_URL}/saveComments`, JSON.stringify(data), options).subscribe(
      (data) => { console.info(data)
      }
    );
    return this.http.get(`${API_URL}/saveComment`, options)
    .pipe(
      catchError(this.handleError)
        );
}


private handleError(error: HttpErrorResponse) {
    if (error.error instanceof ErrorEvent) {
      // A client-side or network error occurred. Handle it accordingly.
      console.error('An error occurred:', error.error.message);
    } else {
      // The backend returned an unsuccessful response code.
      // The response body may contain clues as to what went wrong,
      console.error(
        `Backend returned code ${error.status}, ` +
        `body was: ${error.error}`);
    }
    // return an observable with a user-facing error message
    return throwError(
      'Something bad happened; please try again later.');
  };

}

