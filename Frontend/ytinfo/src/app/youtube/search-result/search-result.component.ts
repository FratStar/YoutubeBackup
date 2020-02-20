import { Component, OnInit, Input } from '@angular/core';
import { VideoInfo } from '../video-info-module';
import { YoutubeSearchService } from 'src/app/services/youtube-search.service';


@Component({
  selector: 'app-search-result',
  templateUrl: './search-result.component.html',
  styleUrls: ['./search-result.component.css']
})
export class SearchResultComponent implements OnInit {
  @Input() result: VideoInfo;
  comments: any;

  constructor(private youtubesearchservice: YoutubeSearchService ) {}


  ngOnInit(): void {

  }

  onClick(){
    this.youtubesearchservice.saveVideoComments(this.result.id).subscribe(
      (data) => {
        this.comments = data;
        var response = JSON.stringify(data);
        console.log(data);
      }
    )
  }

  onClick2(){
    this.youtubesearchservice.downloadVideoComments(this.result.id).subscribe(
      (data) => {
        this.comments = data;
        var response = JSON.stringify(data);
        console.log(data);
      }
    )
  }


}
