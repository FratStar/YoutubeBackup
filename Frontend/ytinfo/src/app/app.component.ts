import { Component } from '@angular/core';
import { VideoInfo } from './youtube/video-info-module';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  results: VideoInfo[];
  loading: boolean;
  message = '';

  updateResults(results: VideoInfo[]): void {
    this.results = results;
    if (this.results.length === 0) {
      this.message = 'Not found...';
    } else {
      this.message = 'Top 25 results:';
    }
  }
}
